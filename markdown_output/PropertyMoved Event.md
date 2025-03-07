Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyMoved Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) : PropertyMoved Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the index of a specification property is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PropertyMoved As [ProjectSpecificationPropertyEventHandler](topic5934.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim handler As [ProjectSpecificationPropertyEventHandler](topic5934.md)
     
    AddHandler instance.PropertyMoved, handler  
  
C#|   
---|---  
      
    
    public event [ProjectSpecificationPropertyEventHandler](topic5934.md) PropertyMoved  
  
# Event Data

The event handler receives an argument of type [ProjectSpecificationPropertyEventArgs](topic4874.md) containing data related to this event. The following **ProjectSpecificationPropertyEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SpecificationProperty](topic4884.md)| Gets the property that was affected by the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)


