Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [GetComponent Method](topic3036.md) : GetComponent(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component.

Glossary Item Box

Gets the captured component with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetComponent( _
       ByVal _componentId_ As Guid _
    ) As [CapturedComponent](topic6147.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim componentId As Guid
    Dim value As [CapturedComponent](topic6147.md)
     
    value = instance.GetComponent(componentId)  
  
C#|   
---|---  
      
    
    public [CapturedComponent](topic6147.md) GetComponent( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component.

#### Return Value

The component with the specified identifier if it is registered, otherwise a null reference.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The component type is not supported.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3036.md)


