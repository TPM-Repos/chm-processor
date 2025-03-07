Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeMetadata Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : InitializeMetadata Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_element_
    The XML element containing the serialized meta data.

Glossary Item Box

Called when the backing store for this task has been initialized and the meta data is available to be read. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub InitializeMetadata( _
       ByVal _element_ As XElement _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim element As XElement
     
    instance.InitializeMetadata(element)  
  
C#|   
---|---  
      
    
    protected virtual void InitializeMetadata( 
       XElement _element_
    )  
  
#### Parameters

 _element_
    The XML element containing the serialized meta data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


