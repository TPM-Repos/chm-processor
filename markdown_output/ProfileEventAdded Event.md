Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProfileEventAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : ProfileEventAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a logical event is started. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ProfileEventAdded As EventHandler(Of ProjectProfileEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim handler As EventHandler(Of ProjectProfileEventArgs)
     
    AddHandler instance.ProfileEventAdded, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ProjectProfileEventArgs> ProfileEventAdded  
  
# Event Data

The event handler receives an argument of type [ProjectProfileEventArgs](topic4692.md) containing data related to this event. The following **ProjectProfileEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ProfileEvent](topic4701.md)| Gets the project profile event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)


