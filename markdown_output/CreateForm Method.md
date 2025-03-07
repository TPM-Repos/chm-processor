Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateForm Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : CreateForm Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the new form.

Glossary Item Box

Creates a new form. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function CreateForm( _
       ByVal _name_ As String _
    ) As [FormNavigationStep](topic10153.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim value As [FormNavigationStep](topic10153.md)
     
    value = instance.CreateForm(name)  
  
C#|   
---|---  
      
    
    public abstract [FormNavigationStep](topic10153.md) CreateForm( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the new form.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


