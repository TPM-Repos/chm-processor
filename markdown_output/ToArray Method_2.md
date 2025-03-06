       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ToArray Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11732.md)  
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

©2024 DriveWorks Ltd. All Rights Reserved.
