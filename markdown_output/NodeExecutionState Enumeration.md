Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum NodeExecutionState 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeExecutionState](topic6900.md)  
  
C#|   
---|---  
      
    
    public enum NodeExecutionState : System.Enum   
  
# Members

Member| Description  
---|---  
**Failed**|  The execution of the [ExecutableNodeBase](topic6938.md) failed.  
**InputsMissing**|  The [ExecutableNodeBase](topic6938.md) has inputs that need to be fulfilled before the [ExecutableNodeBase](topic6938.md) can execute.  
**NotStarted**|  The [ExecutableNodeBase](topic6938.md) is ready to be executed.  
**Skipped**|  The [ExecutableNodeBase](topic6938.md)'s inputs were never fulfilled and thus it was never executed.  
**Successful**|  The execution of the [ExecutableNodeBase](topic6938.md) was successful.  
**SuccessfulWithWarnings**|  The execution of the [ExecutableNodeBase](topic6938.md) was successful but there are some warnings.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.EventFlow.NodeExecutionState**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.EventFlow Namespace](topic6871.md)


