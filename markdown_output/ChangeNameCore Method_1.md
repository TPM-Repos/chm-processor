Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangeNameCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [NavigationStep Class](topic10175.md) : ChangeNameCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newName_
    The new name to apply.

Glossary Item Box

When overridden by a derived class, changes the name of the navigation step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub ChangeNameCore( _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NavigationStep](topic10175.md)
    Dim newName As String
     
    instance.ChangeNameCore(newName)  
  
C#|   
---|---  
      
    
    protected virtual void ChangeNameCore( 
       string _newName_
    )  
  
#### Parameters

 _newName_
    The new name to apply.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStep Class](topic10175.md)   
[NavigationStep Members](topic10176.md)


