using UnityEngine;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

using UnityEngine.Events;

public class HandTracking : MonoBehaviour
{
    public UnityEvent eventIsDropping, eventIsPicking;

    public bool isDropping = true; // true = default pose
    int handPose = 0; // dropping = 0; picking = 1

    float lastValue = 0;
    float x5 = 0;
    // Định nghĩa một sự kiện để thông báo rằng điều kiện dữ liệu đã đạt được
    public static event Action OnHandDataConditionMet;
    
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] handPoints;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;

        if (data.Length > 0) 
        {
            data = data.Remove(0, 1);
            data = data.Remove(data.Length-1, 1);
          //  print(data);
            string[] points = data.Split(',');
          //  print(points[0]);

            //Point 0 - Wrist - Done
            float x = 55-float.Parse(points[0])/10;
            float y = -(-10+float.Parse(points[1])/30);
            float z = 8-float.Parse(points[2])/30;
            handPoints[0].transform.localPosition = new Vector3(x, y, z);

            // HandPoint2 - Thumb - Done
            float x2 = float.Parse(points[6]);
            float y2 = float.Parse(points[7]);
            float z2 = float.Parse(points[8]); 
            handPoints[2].transform.localRotation = Quaternion.Euler(x2, y2, z2);

            // Kiểm tra xem giá trị x2, y2, z2 có đạt giá trị cụ thể không
            // if (x2 == 26.363f && y2 == -77.289f && z2 == 83.927f)
            // {
            //     // Gửi sự kiện khi điều kiện đạt được
            //     if (OnHandDataConditionMet != null)
            //     {
            //         OnHandDataConditionMet();
            //     }
            // }

            // HandPoint3 - Thumb2 - Khong su dung (9,10,11)
            float x3 = float.Parse(points[9]); //-> Need change
            float y3 = float.Parse(points[10]);
            float z3 = float.Parse(points[11]);
            handPoints[3].transform.localRotation = Quaternion.Euler(x3, y3, z3);

            // HandPoint4 - Bone.003_end - Khong su dung (12,13,14)
            float x4 = float.Parse(points[12]); //-> Need change
            float y4 = float.Parse(points[13]);
            float z4 = float.Parse(points[14]);
            handPoints[4].transform.localRotation = Quaternion.Euler(x4, y4, z4);

            // handPoint5 IndexFinger (15,16,17)
            lastValue = x5;

            x5 = float.Parse(points[15]); 
            float y5 = float.Parse(points[16]);
            float z5 = float.Parse(points[17]);
            handPoints[5].transform.localRotation = Quaternion.Euler(x5, y5, z5);

            if(lastValue != x5)
            {
                isDropping = !isDropping;
                
                if(isDropping)
                {
                    eventIsDropping.Invoke();
                }
                else
                {
                    eventIsPicking.Invoke();
                }
            }

           
            // handPoints6 - Index2
            float x6 = float.Parse(points[18]);
            float y6 = float.Parse(points[19]);
            float z6 = float.Parse(points[20]);
            handPoints[6].transform.localRotation = Quaternion.Euler(x6, y6, z6);

            // handPoints7 - Index3
            float x7 = float.Parse(points[21]);
            float y7 = float.Parse(points[22]);
            float z7 = float.Parse(points[23]);
            handPoints[7].transform.localRotation = Quaternion.Euler(x7, y7, z7);

            // handPoints7 - Index3
            float x8 = float.Parse(points[24]);
            float y8 = float.Parse(points[25]);
            float z8 = float.Parse(points[26]);
            handPoints[8].transform.localRotation = Quaternion.Euler(x8, y8, z8);

            // handPoints7 - Index3
            float x9 = float.Parse(points[27]);
            float y9 = float.Parse(points[28]);
            float z9 = float.Parse(points[29]);
            handPoints[9].transform.localRotation = Quaternion.Euler(x9, y9, z9);

            // handPoints7 - Index3
            float x10 = float.Parse(points[30]);
            float y10 = float.Parse(points[31]);
            float z10 = float.Parse(points[32]);
            handPoints[10].transform.localRotation = Quaternion.Euler(x10, y10, z10);

            // handPoints7 - Index3
            float x11 = float.Parse(points[33]);
            float y11 = float.Parse(points[34]);
            float z11 = float.Parse(points[35]);
            handPoints[11].transform.localRotation = Quaternion.Euler(x11, y11, z11);

            // handPoints7 - Index3
            float x12 = float.Parse(points[36]);
            float y12 = float.Parse(points[37]);
            float z12 = float.Parse(points[38]);
            handPoints[12].transform.localRotation = Quaternion.Euler(x12, y12, z12);

            // handPoints7 - Index3
            float x13 = float.Parse(points[39]);
            float y13 = float.Parse(points[40]);
            float z13 = float.Parse(points[41]);
            handPoints[13].transform.localRotation = Quaternion.Euler(x13, y13, z13);

            // handPoints7 - Index3
            float x14 = float.Parse(points[42]);
            float y14 = float.Parse(points[43]);
            float z14 = float.Parse(points[44]);
            handPoints[14].transform.localRotation = Quaternion.Euler(x14, y14, z14);

            // handPoints7 - Index3
            float x15 = float.Parse(points[45]);
            float y15 = float.Parse(points[46]);
            float z15 = float.Parse(points[47]);
            handPoints[15].transform.localRotation = Quaternion.Euler(x15, y15, z15);

            // handPoints7 - Index3
            float x16 = float.Parse(points[48]);
            float y16 = float.Parse(points[49]);
            float z16 = float.Parse(points[50]);
            handPoints[16].transform.localRotation = Quaternion.Euler(x16, y16, z16);

            // handPoints7 - Index3
            // Pinky Finger - point 17-20
            float x17 = float.Parse(points[51]);
            float y17 = float.Parse(points[52]);
            float z17 = float.Parse(points[53]);
            handPoints[17].transform.localRotation = Quaternion.Euler(x17, y17, z17);

            float x18 = float.Parse(points[54]);
            float y18 = float.Parse(points[55]);
            float z18 = float.Parse(points[56]);
            handPoints[18].transform.localRotation = Quaternion.Euler(x18, y18, z18);

            float x19 = float.Parse(points[57]);
            float y19 = float.Parse(points[58]);
            float z19 = float.Parse(points[59]);
            handPoints[19].transform.localRotation = Quaternion.Euler(x19, y19, z19);

            float x20 = float.Parse(points[60]);
            float y20 = float.Parse(points[61]);
            float z20 = float.Parse(points[62]);
            handPoints[20].transform.localRotation = Quaternion.Euler(x20, y20, z20);

        }               
    }
}
