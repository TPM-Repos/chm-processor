Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HasChangesChanged Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [IComponentManager Interface](topic13385.md) : HasChangesChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever the value of the [HasChanges](topic13408.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event HasChangesChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IComponentManager](topic13385.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.HasChangesChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> HasChangesChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IComponentManager Interface](topic13385.md)   
[IComponentManager Members](topic13386.md)


