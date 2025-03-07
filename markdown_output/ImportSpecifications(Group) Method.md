Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ImportSpecifications(Group) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [ImportSpecifications Method](topic3388.md) : ImportSpecifications(Group) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceGroup_
    The group to export specifications from.

Glossary Item Box

Imports all the specifications from the source group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub ImportSpecifications( _
       ByVal _sourceGroup_ As [Group](topic2958.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim sourceGroup As [Group](topic2958.md)
     
    instance.ImportSpecifications(sourceGroup)  
  
C#|   
---|---  
      
    
    public void ImportSpecifications( 
       [Group](topic2958.md) _sourceGroup_
    )  
  
#### Parameters

 _sourceGroup_
    The group to export specifications from.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException|  Thrown when the current group contains specifications.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3388.md)


