       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
States Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [RequiredStatesAttribute Class](topic13901.md) : States Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the list of application states the application is required to be in for this entity to be visible. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property States As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RequiredStatesAttribute](topic13901.md)
    Dim value() As String
     
    value = instance.States  
  
C#|   
---|---  
      
    
    public string[] States {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RequiredStatesAttribute Class](topic13901.md)   
[RequiredStatesAttribute Members](topic13902.md)


