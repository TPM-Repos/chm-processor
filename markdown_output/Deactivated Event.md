Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Deactivated Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureViewEnvironment Interface](topic13353.md) : Deactivated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised whenever the associated view is deactivated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Deactivated As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICaptureViewEnvironment](topic13353.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.Deactivated, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> Deactivated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICaptureViewEnvironment Interface](topic13353.md)   
[ICaptureViewEnvironment Members](topic13354.md)


