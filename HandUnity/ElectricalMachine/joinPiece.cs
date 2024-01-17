using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class joinPiece : MonoBehaviour
{
    public string pieceName;
    private GameObject piece;
    public bool isJoined = false;
    // Start is called before the first frame update
    void OnTriggerEnter(Collider other)
    {
        if(pieceName == other.gameObject.name)
        {
            isJoined = true;
            piece = other.gameObject;

            other.gameObject.GetComponent<PuzzlePiece>().isDone = true;

            // piece.gameObject.transform.localPosition = piece.gameObject.GetComponent<PuzzlePiece>().goalTransform;
            other.transform.SetParent(this.transform);
        }
    }

    void LateUpdate()
    {
       if(isJoined)
           piece.gameObject.transform.localPosition = piece.gameObject.GetComponent<PuzzlePiece>().goalTransform;
    }
}







