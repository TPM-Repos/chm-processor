Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConstantCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) : ConstantCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a constant is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConstantCreated As [ConstantChangedEventHandler](topic5929.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim handler As [ConstantChangedEventHandler](topic5929.md)
     
    AddHandler instance.ConstantCreated, handler  
  
C#|   
---|---  
      
    
    public event [ConstantChangedEventHandler](topic5929.md) ConstantCreated  
  
# Event Data

The event handler receives an argument of type [ConstantEventArgs](topic2595.md) containing data related to this event. The following **ConstantEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Constant](topic2605.md)| Gets the constant that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)


