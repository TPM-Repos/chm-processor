Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : PropertyChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a property is changed, such as name or row count. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PropertyChanged As PropertyChangedEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTable](topic3926.md)
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

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


