Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetStep Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : GetStep Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the step to retrieve.

Glossary Item Box

Gets the named navigation step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetStep( _
       ByVal _name_ As String _
    ) As [NavigationStep](topic10175.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim value As [NavigationStep](topic10175.md)
     
    value = instance.GetStep(name)  
  
C#|   
---|---  
      
    
    public [NavigationStep](topic10175.md) GetStep( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the step to retrieve.

#### Return Value

The named instance of the [NavigationStep](topic10175.md).

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| Thrown when the named navigation step does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


