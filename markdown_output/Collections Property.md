Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Collections Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) : Collections Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the task collections this accessor manages. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected ReadOnly Property Collections As Dictionary(Of ComponentTaskSequenceLocation,ComponentTaskCollection)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim value As Dictionary(Of ComponentTaskSequenceLocation,ComponentTaskCollection)
     
    value = instance.Collections  
  
C#|   
---|---  
      
    
    protected Dictionary<ComponentTaskSequenceLocation,ComponentTaskCollection> Collections {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)


