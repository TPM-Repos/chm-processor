Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyChanged Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified.UI.ReportViewer Namespace](topic15361.md) > [ReportItemBase Class](topic15376.md) : PropertyChanged Event  
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
      
    
    Dim instance As [ReportItemBase](topic15376.md)
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

[ReportItemBase Class](topic15376.md)   
[ReportItemBase Members](topic15377.md)


