Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Extract Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ProjectComponents Class](topic6229.md) : Extract Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentType_
    The type of component to remove.

Glossary Item Box

Removes components of the specified type from the collection and returns them in a new collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Extract( _
       ByVal _componentType_ As String _
    ) As [ProjectComponents](topic6229.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponents](topic6229.md)
    Dim componentType As String
    Dim value As [ProjectComponents](topic6229.md)
     
    value = instance.Extract(componentType)  
  
C#|   
---|---  
      
    
    public [ProjectComponents](topic6229.md) Extract( 
       string _componentType_
    )  
  
#### Parameters

 _componentType_
    The type of component to remove.

#### Return Value

A collection containing the extracted components.

# Remarks

This method will cause all immediate children's capture data to be resolved.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponents Class](topic6229.md)   
[ProjectComponents Members](topic6230.md)


