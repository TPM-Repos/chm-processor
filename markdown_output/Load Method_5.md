Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : Load Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to deserialize and read the information from.

Glossary Item Box

Reads the information stored about the triggered action from the specified task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Load( _
       ByVal _task_ As [SpecificationTaskDetails](topic11510.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim task As [SpecificationTaskDetails](topic11510.md)
     
    instance.Load(task)  
  
C#|   
---|---  
      
    
    public void Load( 
       [SpecificationTaskDetails](topic11510.md) _task_
    )  
  
#### Parameters

 _task_
    The task to deserialize and read the information from.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)


