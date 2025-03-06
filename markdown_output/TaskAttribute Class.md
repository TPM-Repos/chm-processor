TaskAttribute Class   
[Members](topic11660.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : TaskAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides descriptive information about a task. 

# Object Model

![](dotnetdiagramimages/image596.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class TaskAttribute 
       Inherits [DriveWorks.FlowNodeAttribute](topic2887.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskAttribute](topic11659.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class TaskAttribute : [DriveWorks.FlowNodeAttribute](topic2887.md)   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.FlowNodeAttribute](topic2887.md)  
**DriveWorks.Specification.TaskAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskAttribute Members](topic11660.md)   
[DriveWorks.Specification Namespace](topic10764.md)


