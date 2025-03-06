![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeTaskSequenceOrder Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13015.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeTaskSequenceOrder Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskSequenceRef_
    The reference to the task sequence to modify.

_oldIndex_
    The index of the object to move.

_newIndex_
    The index of the where to move the object.

Glossary Item Box

Creates a transaction which, when committed, will update the task sqeuence for the parent object by moving the object at the old index to the new index 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeTaskSequenceOrder( _
       ByVal _taskSequenceRef_ As [TaskSequenceRef](topic13159.md), _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskSequenceRef As [TaskSequenceRef](topic13159.md)
    Dim oldIndex As Integer
    Dim newIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeTaskSequenceOrder(taskSequenceRef, oldIndex, newIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeTaskSequenceOrder( 
       [TaskSequenceRef](topic13159.md) _taskSequenceRef_ ,
       int _oldIndex_ ,
       int _newIndex_
    )  
  
#### Parameters

 _taskSequenceRef_
    The reference to the task sequence to modify.
_oldIndex_
    The index of the object to move.
_newIndex_
    The index of the where to move the object.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
