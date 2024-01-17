using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandController : MonoBehaviour
{
    public HandTracking handTracking;
    //public bool isHolding = false;
    private List<Transform> heldObjects = new List<Transform>();
    private List<Vector3> offsets = new List<Vector3>();
    private Dictionary<Transform, Vector3> initialPositions = new Dictionary<Transform, Vector3>();

    public void Update()
    {

    }

    public void OnTriggerStay(Collider other)
    {
        if (!handTracking.isDropping)
        {
            if(other.gameObject.tag == "grabbable")
            {
                if(other.gameObject.GetComponent<PuzzlePiece>().isDone == false)
                {
                    Debug.Log("collider is a grabbable");
                    other.transform.SetParent(this.transform);
                }
            }
        }

        if (handTracking.isDropping)
        {
            if(other.gameObject.tag == "grabbable")
            {
                if(other.gameObject.GetComponent<PuzzlePiece>().isDone == false)
                {
                    other.transform.SetParent(null);
                }
            }
        }
    }
}
