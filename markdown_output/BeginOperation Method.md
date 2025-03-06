![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginOperation Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISolidWorksOperationBatch Interface](topic1755.md) : BeginOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_priority_
    The priority of this operation relative to others.

_type_
    The type of the operation.

Glossary Item Box

Notifies the SolidWorks Health Monitor of the intention to start a model generation operation. This method call blocks the current thread until exclusive access to SolidWorks is available. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function BeginOperation( _
       ByVal _priority_ As [SolidWorksOperationPriority](topic1808.md), _
       ByVal _type_ As [SolidWorksOperationType](topic1809.md) _
    ) As [ISolidWorksOperation](topic1748.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksOperationBatch](topic1755.md)
    Dim priority As [SolidWorksOperationPriority](topic1808.md)
    Dim type As [SolidWorksOperationType](topic1809.md)
    Dim value As [ISolidWorksOperation](topic1748.md)
     
    value = instance.BeginOperation(priority, type)  
  
C#|   
---|---  
      
    
    [ISolidWorksOperation](topic1748.md) BeginOperation( 
       [SolidWorksOperationPriority](topic1808.md) _priority_ ,
       [SolidWorksOperationType](topic1809.md) _type_
    )  
  
#### Parameters

 _priority_
    The priority of this operation relative to others.
_type_
    The type of the operation.

#### Return Value

An operation which can be used to coordinate the execution of the operation with the SolidWorks Health Monitor.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISolidWorksOperationBatch Interface](topic1755.md)   
[ISolidWorksOperationBatch Members](topic1756.md)


