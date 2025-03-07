Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Added Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskCollection Class](topic6466.md) : Added Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised when a task has been added to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Added As EventHandler(Of ComponentTaskEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskCollection](topic6466.md)
    Dim handler As EventHandler(Of ComponentTaskEventArgs)
     
    AddHandler instance.Added, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ComponentTaskEventArgs> Added  
  
# Event Data

The event handler receives an argument of type [ComponentTaskEventArgs](topic6596.md) containing data related to this event. The following **ComponentTaskEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Task](topic6602.md)| Gets the task associated with this event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskCollection Class](topic6466.md)   
[ComponentTaskCollection Members](topic6467.md)


