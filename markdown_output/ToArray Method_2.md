ToArray Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) : ToArray Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Copies the tasks to a new array and returns it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ToArray() As [Task()](topic11629.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim value() As [Task](topic11629.md)
     
    value = instance.ToArray()  
  
C#|   
---|---  
      
    
    public [Task[]](topic11629.md) ToArray()  
  
#### Return Value

A new array containing all the tasks in this instance.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)


