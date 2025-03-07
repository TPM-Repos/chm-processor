Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) > [Item Property](topic4843.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_propertyName_
    The name of the item to get.

Glossary Item Box

Gets the item with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _propertyName_ As String _
    ) As [ProjectSpecificationProperty](topic4853.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim propertyName As String
    Dim value As [ProjectSpecificationProperty](topic4853.md)
     
    value = instance.Item(propertyName)  
  
C#|   
---|---  
      
    
    public [ProjectSpecificationProperty](topic4853.md) Item( 
       string _propertyName_
    ) {get;}  
  
#### Parameters

 _propertyName_
    The name of the item to get.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| An item with the given name does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)   
[Overload List](topic4843.md)


