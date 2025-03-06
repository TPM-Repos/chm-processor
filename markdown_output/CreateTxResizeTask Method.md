![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxResizeTask Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13130.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxResizeTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskRef_
    The reference to the task to modify.

_newWidth_
    The new width of the task.

Glossary Item Box

Creates a transaction which, when committed, will change the size of the specified task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxResizeTask( _
       ByVal _taskRef_ As [TaskRef](topic13149.md), _
       ByVal _newWidth_ As Nullable(Of Double) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskRef As [TaskRef](topic13149.md)
    Dim newWidth As Nullable(Of Double)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxResizeTask(taskRef, newWidth)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxResizeTask( 
       [TaskRef](topic13149.md) _taskRef_ ,
       Nullable<double> _newWidth_
    )  
  
#### Parameters

 _taskRef_
    The reference to the task to modify.
_newWidth_
    The new width of the task.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
