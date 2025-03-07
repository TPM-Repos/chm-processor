Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CellValueChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : CellValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a cell's value is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CellValueChanged As EventHandler(Of CellValueChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTable](topic3926.md)
    Dim handler As EventHandler(Of CellValueChangedEventArgs)
     
    AddHandler instance.CellValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<CellValueChangedEventArgs> CellValueChanged  
  
# Event Data

The event handler receives an argument of type [CellValueChangedEventArgs](topic2479.md) containing data related to this event. The following **CellValueChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[X](topic2485.md)| The horizontal location of the cell.   
[Y](topic2486.md)| The vertical location of the cell.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


