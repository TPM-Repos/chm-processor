Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnPriorityTagsRemoved Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : OnPriorityTagsRemoved Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tags_
    

Glossary Item Box

Raises the [PriorityTagsRemoved](topic1686.md) event with the provided collection of removed tags. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OnPriorityTagsRemoved( _
       ByVal _tags_ As IEnumerable(Of String) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim tags As IEnumerable(Of String)
     
    instance.OnPriorityTagsRemoved(tags)  
  
C#|   
---|---  
      
    
    void OnPriorityTagsRemoved( 
       IEnumerable<string> _tags_
    )  
  
#### Parameters

 _tags_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


