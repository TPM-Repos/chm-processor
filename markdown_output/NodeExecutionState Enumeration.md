![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NodeExecutionState Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : NodeExecutionState Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the state of a [ExecutableNodeBase](topic6938.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum NodeExecutionState 
       Inherits System.Enum  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeExecutionState](topic6900.md)  
  
C#|   
---|---  
      
    
    public enum NodeExecutionState : System.Enum   
  
# ![](dotnetimages/collapse.gif)Members

Member| Description  
---|---  
**Failed**|  The execution of the [ExecutableNodeBase](topic6938.md) failed.  
**InputsMissing**|  The [ExecutableNodeBase](topic6938.md) has inputs that need to be fulfilled before the [ExecutableNodeBase](topic6938.md) can execute.  
**NotStarted**|  The [ExecutableNodeBase](topic6938.md) is ready to be executed.  
**Skipped**|  The [ExecutableNodeBase](topic6938.md)'s inputs were never fulfilled and thus it was never executed.  
**Successful**|  The execution of the [ExecutableNodeBase](topic6938.md) was successful.  
**SuccessfulWithWarnings**|  The execution of the [ExecutableNodeBase](topic6938.md) was successful but there are some warnings.  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.EventFlow.NodeExecutionState**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.EventFlow Namespace](topic6871.md)


