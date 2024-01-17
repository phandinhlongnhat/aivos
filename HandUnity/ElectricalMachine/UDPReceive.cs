using UnityEngine;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class UDPReceive : MonoBehaviour
{

    Thread receiveThread;
    UdpClient client; 
    public int port = 5052;
    public bool startRecieving = true;
    public bool printToConsole = false;
    public string data;


    public void Start()
    {

        receiveThread = new Thread(
            new ThreadStart(ReceiveData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
    }


    private readonly object lockObject = new object();  // Đối tượng để lock

    // receive thread
    private void ReceiveData()
    {
        client = new UdpClient(port);
        while (startRecieving)
        {
          try
          {
            IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
            byte[] dataByte = client.Receive(ref anyIP);

            // Lock để đảm bảo an toàn khi truy cập data
            lock (lockObject)
            {
                data = Encoding.UTF8.GetString(dataByte);
            }

            if (printToConsole)
            {
                Debug.Log(data);
            }
          }
          catch (Exception err)
          {
            Debug.LogError(err.ToString());
          }
        }
    }
}