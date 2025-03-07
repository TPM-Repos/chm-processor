Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateRenameProcess Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : CreateRenameProcess Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldNames_
    The names which are being replaced.

_newNames_
    The names which replace the old names.

Glossary Item Box

Creates a new process capable of swapping out one set of names in all the rules in the project, for another set of names. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateRenameProcess( _
       ByVal _oldNames_() As String, _
       ByVal _newNames_() As String _
    ) As [RenameProcess](topic10287.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim oldNames() As String
    Dim newNames() As String
    Dim value As [RenameProcess](topic10287.md)
     
    value = instance.CreateRenameProcess(oldNames, newNames)  
  
C#|   
---|---  
      
    
    public [RenameProcess](topic10287.md) CreateRenameProcess( 
       string[] _oldNames_ ,
       string[] _newNames_
    )  
  
#### Parameters

 _oldNames_
    The names which are being replaced.
_newNames_
    The names which replace the old names.

#### Return Value

An instance of the [DriveWorks.Refactoring.RenameProcess](topic10287.md) class which will perform the renaming.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


