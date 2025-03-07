Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentDetailsByPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentDetailsByPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The full path to the component for which to get the details.

_throwIfMissing_
    Throws an exception if a component with the specified path cannot be found, if false, a null reference is returned if the component isn't found.

Glossary Item Box

Get's the component details for a component with the specified path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentDetailsByPath( _
       ByVal _path_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [ReleasedComponentDetails](topic6336.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim path As String
    Dim throwIfMissing As Boolean
    Dim value As [ReleasedComponentDetails](topic6336.md)
     
    value = instance.GetComponentDetailsByPath(path, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [ReleasedComponentDetails](topic6336.md) GetComponentDetailsByPath( 
       string _path_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _path_
    The full path to the component for which to get the details.
_throwIfMissing_
    Throws an exception if a component with the specified path cannot be found, if false, a null reference is returned if the component isn't found.

#### Return Value

The component's details.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| No component could be found with the specified path.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


