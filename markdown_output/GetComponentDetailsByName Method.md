![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentDetailsByName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentDetailsByName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the component for which to get the details.

_type_
    The type of the component for which to get the details.

_throwIfMissing_
    Throws an exception if a component with the specified name and type cannot be found, if false, a null reference is returned if the component isn't found.

Glossary Item Box

Get's the component details for a component with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentDetailsByName( _
       ByVal _name_ As String, _
       ByVal _type_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [ReleasedComponentDetails](topic6336.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim name As String
    Dim type As String
    Dim throwIfMissing As Boolean
    Dim value As [ReleasedComponentDetails](topic6336.md)
     
    value = instance.GetComponentDetailsByName(name, type, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [ReleasedComponentDetails](topic6336.md) GetComponentDetailsByName( 
       string _name_ ,
       string _type_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _name_
    The name of the component for which to get the details.
_type_
    The type of the component for which to get the details.
_throwIfMissing_
    Throws an exception if a component with the specified name and type cannot be found, if false, a null reference is returned if the component isn't found.

#### Return Value

The component's details.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| No component could be found with the specified name and type.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


