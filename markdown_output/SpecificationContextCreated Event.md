       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationContextCreated Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationService Interface](topic489.md) : SpecificationContextCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a specification context is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SpecificationContextCreated As [SpecificationContextEventHandler](topic11821.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationService](topic489.md)
    Dim handler As [SpecificationContextEventHandler](topic11821.md)
     
    AddHandler instance.SpecificationContextCreated, handler  
  
C#|   
---|---  
      
    
    event [SpecificationContextEventHandler](topic11821.md) SpecificationContextCreated  
  
# Event Data

The event handler receives an argument of type [SpecificationContextEventArgs](topic11284.md) containing data related to this event. The following **SpecificationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic11291.md)| Get the specification context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationService Interface](topic489.md)   
[ISpecificationService Members](topic490.md)


