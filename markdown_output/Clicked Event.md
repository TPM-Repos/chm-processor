Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Clicked Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButton Interface](topic115.md) : Clicked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the command button is clicked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Clicked As MouseEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandButton](topic115.md)
    Dim handler As MouseEventHandler
     
    AddHandler instance.Clicked, handler  
  
C#|   
---|---  
      
    
    event MouseEventHandler Clicked  
  
# Event Data

The event handler receives an argument of type MouseEventArgs containing data related to this event. The following **MouseEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Button|   
Clicks|   
Delta|   
Location|   
X|   
Y|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandButton Interface](topic115.md)   
[ICommandButton Members](topic116.md)


