Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveAppDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : DriveAppDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a DriveApp is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event DriveAppDeleted As EventHandler(Of ValueEventArgs(Of Guid))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim handler As EventHandler(Of ValueEventArgs(Of Guid))
     
    AddHandler instance.DriveAppDeleted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueEventArgs<Guid>> DriveAppDeleted  
  
# Event Data

The event handler receives an argument of type [ValueEventArgs<T>](topic5843.md) containing data related to this event. The following **ValueEventArgs <T>** properties provide information specific to this event.

Property| Description  
---|---  
[Value](topic5850.md)| Gets the item specific to this event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


