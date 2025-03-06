TaskExecutionResult Enumeration   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : TaskExecutionResult Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the execution result of a [GenerationTask](topic13678.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum TaskExecutionResult 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskExecutionResult](topic13454.md)  
  
C#|   
---|---  
      
    
    public enum TaskExecutionResult : System.Enum   
  
# Members

Member| Description  
---|---  
**Failed**|  Indicates that the task failed to execute.  
**Success**|  Indicates that the task successfully ran to completion.  
**SuccessfulIgnored**|  Indicates that the task was not required to execute.  
**SuccessWithWarnings**|  Indicates that the task was successful, but one or multiple warnings were raised.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.SolidWorks.TaskExecutionResult**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.SolidWorks Namespace](topic13345.md)


