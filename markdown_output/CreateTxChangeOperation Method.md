![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The operation to update.

_newTitle_
    The new title of the operation.

_newConditons_
    The new conditions for the operation.

_newTaskSequence_
    The new tasks for the operation.

Glossary Item Box

Creates a transaction which, when committed, will update an operation with given parameters. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeOperation( _
       ByVal _operation_ As [Operation](topic11068.md), _
       ByVal _newTitle_ As String, _
       ByVal _newConditons_() As [Condition](topic10804.md), _
       ByVal _newTaskSequence_() As [Task](topic11629.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim operation As [Operation](topic11068.md)
    Dim newTitle As String
    Dim newConditons() As [Condition](topic10804.md)
    Dim newTaskSequence() As [Task](topic11629.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeOperation(operation, newTitle, newConditons, newTaskSequence)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeOperation( 
       [Operation](topic11068.md) _operation_ ,
       string _newTitle_ ,
       [Condition](topic10804.md)[] _newConditons_ ,
       [Task](topic11629.md)[] _newTaskSequence_
    )  
  
#### Parameters

 _operation_
    The operation to update.
_newTitle_
    The new title of the operation.
_newConditons_
    The new conditions for the operation.
_newTaskSequence_
    The new tasks for the operation.

# ![](dotnetimages/collapse.gif)Remarks

Arguments can be set to nothing if no change is needed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


