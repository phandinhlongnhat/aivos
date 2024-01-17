using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PuzzlePiece : MonoBehaviour
{
    public Vector3 goalTransform;
    public bool isDone = false;
    // Start is called before the first frame update
    public void showMessage(string i)
    {
        Debug.Log(i);
    }
}
