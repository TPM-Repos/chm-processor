Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Disconnected Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksService Interface](topic13411.md) : Disconnected Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when DriveWorks disconnects from the current instance of SolidWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Disconnected As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksService](topic13411.md)
    Dim handler As EventHandler
     
    AddHandler instance.Disconnected, handler  
  
C#|   
---|---  
      
    
    event EventHandler Disconnected  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksService Interface](topic13411.md)   
[ISolidWorksService Members](topic13412.md)


