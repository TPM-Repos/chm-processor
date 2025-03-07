Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitialSpecificationId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariables Class](topic4782.md) : InitialSpecificationId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifier of the initial specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property InitialSpecificationId As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariables](topic4782.md)
    Dim value As Integer
     
    value = instance.InitialSpecificationId  
  
C#|   
---|---  
      
    
    public abstract int InitialSpecificationId {get;}  
  
# Remarks

When specifications are edited and copied, the specification identifier changes, this property provides access to the very first specification identifier if this happens.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariables Class](topic4782.md)   
[ProjectSpecialVariables Members](topic4783.md)


