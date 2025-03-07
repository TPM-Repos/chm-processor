Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteReleasedComponentReports Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : DeleteReleasedComponentReports Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The Id of the component for which all of its reports should be deleted.

Glossary Item Box

Deletes all component reports for the specified component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteReleasedComponentReports( _
       ByVal _componentId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim value As Boolean
     
    value = instance.DeleteReleasedComponentReports(componentId)  
  
C#|   
---|---  
      
    
    public bool DeleteReleasedComponentReports( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The Id of the component for which all of its reports should be deleted.

#### Return Value

True if all reports were deleted successfully.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


