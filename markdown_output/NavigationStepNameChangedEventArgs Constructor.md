Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationStepNameChangedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [NavigationStepNameChangedEventArgs Class](topic10213.md) : NavigationStepNameChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_navigationStep_
    The navigation step that was changed.

_oldName_
    The old name of the navigation step.

_newName_
    The new name of the navigation step.

Glossary Item Box

Initializes a new instance of the [NavigationStepNameChangedEventArgs](topic10213.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _navigationStep_ As [NavigationStep](topic10175.md), _
       ByVal _oldName_ As String, _
       ByVal _newName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim navigationStep As [NavigationStep](topic10175.md)
    Dim oldName As String
    Dim newName As String
     
    Dim instance As New [NavigationStepNameChangedEventArgs](topic10213.md)(navigationStep, oldName, newName)  
  
C#|   
---|---  
      
    
    public NavigationStepNameChangedEventArgs( 
       [NavigationStep](topic10175.md) _navigationStep_ ,
       string _oldName_ ,
       string _newName_
    )  
  
#### Parameters

 _navigationStep_
    The navigation step that was changed.
_oldName_
    The old name of the navigation step.
_newName_
    The new name of the navigation step.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStepNameChangedEventArgs Class](topic10213.md)   
[NavigationStepNameChangedEventArgs Members](topic10214.md)


