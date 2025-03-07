Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Disconnecting Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureViewHost Interface](topic13363.md) : Disconnecting Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the host is disconnecting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Disconnecting As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICaptureViewHost](topic13363.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.Disconnecting, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> Disconnecting  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICaptureViewHost Interface](topic13363.md)   
[ICaptureViewHost Members](topic13364.md)


