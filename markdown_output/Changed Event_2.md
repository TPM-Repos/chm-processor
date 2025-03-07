Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Changed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : Changed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the table changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <CLSCompliantAttribute(False)>
    Public Event Changed As EventHandler(Of TableChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTable](topic3926.md)
    Dim handler As EventHandler(Of TableChangedEventArgs)
     
    AddHandler instance.Changed, handler  
  
C#|   
---|---  
      
    
    [CLSCompliantAttribute(false)]
    public event EventHandler<TableChangedEventArgs> Changed  
  
# Event Data

The event handler receives an argument of type DriveWorksTK.Util.Collections.TableChangedEventArgs containing data related to this event. The following **TableChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
**EventType**|   
**Location**|   
**NewIndex**|   
**OldIndex**|   
**Size**|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


