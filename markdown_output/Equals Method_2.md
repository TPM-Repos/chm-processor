Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Equals Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectListItemData Class](topic4555.md) : Equals Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_obj_
    The ProjectListItemData object to compare to.

Glossary Item Box

Determines whether two ProjectListItemData objects are equal. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function Equals( _
       ByVal _obj_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectListItemData](topic4555.md)
    Dim obj As Object
    Dim value As Boolean
     
    value = instance.Equals(obj)  
  
C#|   
---|---  
      
    
    public override bool Equals( 
       object _obj_
    )  
  
#### Parameters

 _obj_
    The ProjectListItemData object to compare to.

#### Return Value

True if the two objects are equal.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectListItemData Class](topic4555.md)   
[ProjectListItemData Members](topic4556.md)


