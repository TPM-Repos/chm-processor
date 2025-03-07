Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedComponentRefCollection Class](topic14120.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childComponentId_
    The unique identifier of the part or sub-assembly to add as a reference.

Glossary Item Box

Adds a new reference to the specified part or sub-assembly. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _childComponentId_ As Guid _
    ) As [CapturedComponentRef](topic14113.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedComponentRefCollection](topic14120.md)
    Dim childComponentId As Guid
    Dim value As [CapturedComponentRef](topic14113.md)
     
    value = instance.Add(childComponentId)  
  
C#|   
---|---  
      
    
    public [CapturedComponentRef](topic14113.md) Add( 
       Guid _childComponentId_
    )  
  
#### Parameters

 _childComponentId_
    The unique identifier of the part or sub-assembly to add as a reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedComponentRefCollection Class](topic14120.md)   
[CapturedComponentRefCollection Members](topic14121.md)


