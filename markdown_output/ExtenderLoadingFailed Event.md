Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExtenderLoadingFailed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : ExtenderLoadingFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when one or more project extenders failed to load. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ExtenderLoadingFailed As EventHandler(Of List(Of ProjectExtenderLoadException))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim handler As EventHandler(Of List(Of ProjectExtenderLoadException))
     
    AddHandler instance.ExtenderLoadingFailed, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<List<ProjectExtenderLoadException>> ExtenderLoadingFailed  
  
# Event Data

The event handler receives an argument of type List<T> containing data related to this event. The following **List <T>** properties provide information specific to this event.

Property| Description  
---|---  
Capacity|   
Count|   
Item|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


