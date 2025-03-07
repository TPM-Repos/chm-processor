Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetForms Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : GetForms Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includeDialogForms_
    True to include forms which are not linked into the navigation, false to filter them out of the result.

_includeStandardForms_
    True to include forms which are linked into the navigation, false to filter them out of the result.

Glossary Item Box

Gets the project's forms. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetForms( _
       ByVal _includeDialogForms_ As Boolean, _
       ByVal _includeStandardForms_ As Boolean _
    ) As [FormNavigationStep()](topic10153.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim includeDialogForms As Boolean
    Dim includeStandardForms As Boolean
    Dim value() As [FormNavigationStep](topic10153.md)
     
    value = instance.GetForms(includeDialogForms, includeStandardForms)  
  
C#|   
---|---  
      
    
    public [FormNavigationStep[]](topic10153.md) GetForms( 
       bool _includeDialogForms_ ,
       bool _includeStandardForms_
    )  
  
#### Parameters

 _includeDialogForms_
    True to include forms which are not linked into the navigation, false to filter them out of the result.
_includeStandardForms_
    True to include forms which are linked into the navigation, false to filter them out of the result.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


