Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DescendantId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : DescendantId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the identifier of the descendant specification to which the release results belong. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property DescendantId As Nullable(Of Integer)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim value As Nullable(Of Integer)
     
    value = instance.DescendantId  
  
C#|   
---|---  
      
    
    public Nullable<int> DescendantId {get;}  
  
# Remarks

This will return null if we are not an embedded child specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


