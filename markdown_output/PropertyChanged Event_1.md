Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocumentNodeData Class](topic3659.md) : PropertyChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PropertyChanged As PropertyChangedEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JsonDocumentNodeData](topic3659.md)
    Dim handler As PropertyChangedEventHandler
     
    AddHandler instance.PropertyChanged, handler  
  
C#|   
---|---  
      
    
    public event PropertyChangedEventHandler PropertyChanged  
  
# Event Data

The event handler receives an argument of type PropertyChangedEventArgs containing data related to this event. The following **PropertyChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
PropertyName|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JsonDocumentNodeData Class](topic3659.md)   
[JsonDocumentNodeData Members](topic3660.md)


