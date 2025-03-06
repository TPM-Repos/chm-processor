       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetStep(String,NavigationStep) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10245.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) > [TryGetStep Method](topic10243.md) : TryGetStep(String,NavigationStep) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the step to retrieve.

_navigationStep_
    A reference to a variable which will received the retrieved navigation step.

Glossary Item Box

Gets the named navigation step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetStep( _
       ByVal _name_ As String, _
       ByRef _navigationStep_ As [NavigationStep](topic10175.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim navigationStep As [NavigationStep](topic10175.md)
    Dim value As Boolean
     
    value = instance.TryGetStep(name, navigationStep)  
  
C#|   
---|---  
      
    
    public bool TryGetStep( 
       string _name_ ,
       ref [NavigationStep](topic10175.md) _navigationStep_
    )  
  
#### Parameters

 _name_
    The name of the step to retrieve.
_navigationStep_
    A reference to a variable which will received the retrieved navigation step.

#### Return Value

True if the item was successfully retrieved, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)   
[Overload List](topic10243.md)

©2024 DriveWorks Ltd. All Rights Reserved.
